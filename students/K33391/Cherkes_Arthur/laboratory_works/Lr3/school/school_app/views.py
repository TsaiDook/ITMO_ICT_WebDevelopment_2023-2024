from django.db.models import Min, Max
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class TeacherListView(generics.ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class TeacherRetrieveView(generics.RetrieveAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class TeacherCreateView(generics.CreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class TeacherUpdateView(generics.UpdateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class TeacherDeleteView(generics.DestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
#    permission_classes = [permissions.IsAuthenticated, ]




class CabinetListView(generics.ListAPIView):
    queryset = Cabinets.objects.all()
    serializer_class = CabinetSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class CabinetRetrieveView(generics.RetrieveAPIView):
    queryset = Cabinets.objects.all()
    serializer_class = CabinetSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class CabinetCreateView(generics.CreateAPIView):
    queryset = Cabinets.objects.all()
    serializer_class = CabinetSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class CabinetUpdateView(generics.UpdateAPIView):
    queryset = Cabinets.objects.all()
    serializer_class = CabinetSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class CabinetDeleteView(generics.DestroyAPIView):
    queryset = Cabinets.objects.all()
    serializer_class = CabinetSerializer
#    permission_classes = [permissions.IsAuthenticated, ]




class ClassListView(generics.ListAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class ClassRetrieveView(generics.RetrieveAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer
#    permission_classes = [permissions.IsAuthenticated, ]



class ClassCreateView(generics.CreateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class ClassUpdateView(generics.UpdateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class ClassDeleteView(generics.DestroyAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer
#    permission_classes = [permissions.IsAuthenticated, ]



class StudentListView(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
#    permission_classes = [permissions.IsAuthenticated, ]


class StudentRetrieveView(generics.RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class StudentCreateView(generics.CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class StudentUpdateView(generics.UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class StudentDeleteView(generics.DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
#    permission_classes = [permissions.IsAuthenticated, ]




class ScheduleListView(generics.ListAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class ScheduleRetrieveView(generics.RetrieveAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class ScheduleCreateView(generics.CreateAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class ScheduleUpdateView(generics.UpdateAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class ScheduleDeleteView(generics.DestroyAPIView):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer
#    permission_classes = [permissions.IsAuthenticated, ]




class TeachingListView(generics.ListAPIView):
    queryset = Teachings.objects.all()
    serializer_class = TeachingSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class TeachingRetrieveView(generics.RetrieveAPIView):
    queryset = Teachings.objects.all()
    serializer_class = TeachingSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class TeachingCreateView(generics.CreateAPIView):
    queryset = Teachings.objects.all()
    serializer_class = TeachingSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class TeachingUpdateView(generics.UpdateAPIView):
    queryset = Teachings.objects.all()
    serializer_class = TeachingSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class TeachingDeleteView(generics.DestroyAPIView):
    queryset = Teachings.objects.all()
    serializer_class = TeachingSerializer
#    permission_classes = [permissions.IsAuthenticated, ]




class SubjectListView(generics.ListAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class SubjectRetrieveView(generics.RetrieveAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class SubjectCreateView(generics.CreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class SubjectUpdateView(generics.UpdateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class SubjectDeleteView(generics.DestroyAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
#    permission_classes = [permissions.IsAuthenticated, ]


class SpecialStudentListView(generics.ListAPIView):
    serializer_class = StudentSerializer
#    permission_classes = [permissions.IsAuthenticated, ]
    def get_queryset(self):
       grade = self.kwargs['grade']
       studs = Students.objects.filter(grades__grade__contains = grade )
       return studs


class GradeListView(generics.ListAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradeSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class GradeRetrieveView(generics.RetrieveAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradeSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class GradeCreateView(generics.CreateAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradeSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class GradeUpdateView(generics.UpdateAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradeSerializer
#    permission_classes = [permissions.IsAuthenticated, ]

class GradeDeleteView(generics.DestroyAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradeSerializer
#    permission_classes = [permissions.IsAuthenticated, ]



class LogOut(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)