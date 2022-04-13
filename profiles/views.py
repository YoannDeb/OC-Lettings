from django.shortcuts import render

from .models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed
# consequat libero pulvinar eget. Fusc faucibus, urna quis auctor pharetra,
# massa dolor cursus neque, quis dictum lacus d
def index(request):
    """
    Profiles index view, which shows a listing of all profiles.
    :param request: the request sent by the client.
    :return: A render of the profiles' index.html page.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque
# quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus, it. Nam aliquam
# dignissim congue. Pellentesque habitant morbi tristique senectus et netus et
# males
def profile(request, username):
    """
    Profiles profiles view, which shows details about one profile.
    :param request: the request sent by the client.
    :return: A render of the profiles' profile.html page.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
