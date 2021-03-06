from django.urls import path
from dashboard.views import ProfileView, DashboardView, InvestmentView, WithdrawView, deposit, EcalenderView, TsignalView, MkView, support

urlpatterns = [
    path('', DashboardView.as_view(), name='dashb'),
    path('profile/',ProfileView.as_view(), name='profile'),
    path('investment/',InvestmentView.as_view(), name='investment'),
    path('withdraw/',WithdrawView.as_view(), name='withdraw'),
    path('deposit/',deposit, name='deposit'),
    path('ec_calender/',EcalenderView.as_view(), name='ecalender'),
    path('tr_signals/',TsignalView.as_view(), name='tsignal'),
    path('mk_overview/',MkView.as_view(), name='mk_overview'),
    path('support/',support, name='support'),
]

