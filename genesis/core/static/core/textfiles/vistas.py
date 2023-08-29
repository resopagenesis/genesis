from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Sum, Count, Avg, Q, Case, Value, When,ExpressionWrapper
from django.db.models import FloatField,F
from django.db.models.functions import TruncMonth,ExtractMonth, ExtractYear
from django.db.models.functions import Cast, Substr
import random
import datetime
from django import forms
import time
import os
import pickle
import sqlite3
import pandas as pd
import copy

# Reporte
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table,TableStyle, Image, Spacer
from core.views import Reporte
from reportlab.lib.pagesizes import letter,landscape,portrait,A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm, cm
from reportlab.lib import colors
from reportlab.platypus import Flowable, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT

#@[p_view_01]

@importroles
#@[p_view_02]
@importmodelos
#@[p_view_03]
@importforeign
#@[p_view_04]
@importforms
#@[p_view_05]

# Create your views here.
#@[p_view_06]
@modelospadre
#@[p_view_07]

#@[p_view_08]
@modeloshijo
#@[p_view_09]

#@[p_view_10]
@loadhijos
#@[p_view_11]

