from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Faculty, Group, Student, Subject, Teacher, Department
from .forms import FacultyForm, GroupForm, StudentForm, SubjectForm, TeacherForm, DepartmentForm


def home(request):
    faculty_count = Faculty.objects.count()
    department_count = Department.objects.count()
    subject_count = Subject.objects.count()
    teacher_count = Teacher.objects.count()
    group_count = Group.objects.count()
    student_count = Student.objects.count()

    context = {
        'faculty_count': faculty_count,
        'department_count': department_count,
        'subject_count': subject_count,
        'teacher_count': teacher_count,
        'group_count': group_count,
        'student_count': student_count,
    }
    return render(request, 'home.html', context)


def faculty_list(request):
    faculties = Faculty.objects.all()
    ctx = {'faculties': faculties}
    return render(request, 'faculty_list.html', ctx)


def faculty_create(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')  # Redirect to the faculty list after creation
    else:
        form = FacultyForm()

    # Do not pass 'faculty' to the template in the create view
    return render(request, 'faculty_form.html', {'form': form})


def faculty_update(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    else:
        form = FacultyForm(instance=faculty)
    return render(request, 'faculty_form.html', {'form': form, 'faculty': faculty})


def faculty_delete(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        faculty.delete()
        return redirect('faculty_list')
    return render(request, 'faculty_confirm.html', {'faculty': faculty})


def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'group_list.html', ctx)


def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'group_form.html', {'form': form})


def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'group_form.html', {'form': form, 'group': group})


def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('group_list')
    return render(request, 'group_confirm.html', {'group': group})


def department_list(request):
    departments = Department.objects.all()
    ctx = {'departments': departments}
    return render(request, 'department_list.html', ctx)


def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'department_form.html', {'form': form})


def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'department_form.html', {'form': form, 'department': department})


def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'department_confirm.html', {'department': department})


def subject_list(request):
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return render(request, 'subject_list.html', ctx)


def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'subject_form.html', {'form': form})


def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'subject_form.html', {'form': form, 'subject': subject})


def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'subject_confirm.html', {'subject': subject})


def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teacher_list.html', ctx)


def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teacher_form.html', {'form': form})


def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teacher_form.html', {'form': form, 'teacher': teacher})


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'teacher_confirm.html', {'teacher': teacher})


def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'student_list.html', ctx)


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form, 'student': student})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm.html', {'student': student})

