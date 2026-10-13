from django.shortcuts import get_object_or_404, render

from .models import Department, ExchangeProgram, MainPage, Program, Teacher


def index(request):
    page = MainPage.objects.first()
    departments_count = Department.objects.count()
    programs_count = Program.objects.count()
    teachers_count = Teacher.objects.count()
    return render(
        request,
        "faculty/index.html",
        {
            "page": page,
            "departments_count": departments_count,
            "programs_count": programs_count,
            "teachers_count": teachers_count,
        },
    )


def programs(request):
    all_programs = Program.objects.all().order_by("code", "name")
    return render(request, "faculty/programs.html", {"programs": all_programs})


def program_detail(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    return render(request, "faculty/program_detail.html", {"program": program})


def departments(request):
    all_departments = Department.objects.all().order_by("name")
    return render(request, "faculty/departments.html", {"departments": all_departments})


def department_detail(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    teachers = department.teachers.all().order_by("name")
    return render(
        request,
        "faculty/department_detail.html",
        {"department": department, "teachers": teachers},
    )


def exchange(request):
    country = request.GET.get("country", "")
    exchange_programs = ExchangeProgram.objects.all().order_by("deadline")
    if country != "":
        exchange_programs = exchange_programs.filter(country=country)

    countries = []
    for program in ExchangeProgram.objects.all().order_by("country"):
        if program.country not in countries:
            countries.append(program.country)

    return render(
        request,
        "faculty/exchange.html",
        {
            "exchange_programs": exchange_programs,
            "countries": countries,
            "selected_country": country,
        },
    )
