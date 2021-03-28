from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200, null=False)
    father_name = models.CharField(max_length=200, null=False)
    mother_name = models.CharField(max_length=200, null=False)
    address = models.TextField()
    age = models.IntegerField()
    dob = models.DateField(null=False)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_OTHER = 3
    gender_choice = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other'),
    )
    gender = models.IntegerField(choices=gender_choice)
    image = models.ImageField(upload_to='image/', null=False)

    def __str__(self):
        return self.name


class StuClassInfo(models.Model):
    class_name = models.CharField(max_length=10)
    class_short_name = models.CharField(max_length=5)

    def __str__(self):
        return self.class_name


class StuShiftInfo(models.Model):
    shift_name = models.CharField(max_length=20)

    def __str__(self):
        return self.shift_name


class StuDetailsInfo(models.Model):
    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)
    roll = models.IntegerField()
    stu_class = models.ForeignKey(StuClassInfo, on_delete=models.SET_NULL, null=True)
    stu_shift = models.ForeignKey(StuShiftInfo, on_delete=models.SET_NULL, null=True)
    stu_section = models.CharField(max_length=20)
    stu_session = models.IntegerField()

    class Meta:
        unique_together = ['roll', 'stu_class', 'stu_shift', 'stu_section', 'stu_session']

    def __str__(self):
        return self.student.name


class AttendanceManager(models.Manager):
    def create_attendance(self, stu_class, stu_roll):
        stu_obj = StuDetailsInfo.objects.get(stu_class__class_name=stu_class, roll=stu_roll)
        att_obj = Attendance.objects.create(student=stu_obj, status=1)
        return att_obj


class Attendance(models.Model):
    student = models.ForeignKey(StuDetailsInfo, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)

    objects = AttendanceManager()

    class Meta:
        unique_together = ['student', 'date']

    def __str__(self):
        return self.student.student.name
