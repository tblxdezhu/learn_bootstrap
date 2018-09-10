from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def test(request):
    return render(request, 'run_slam_ssa.html', {'if_test_active': 'active'})


@login_required
def step2(request):
    return render(request, 'step2.html', {'if_test_active': 'active'})
