'''
The MIT License (MIT)

Copyright (c) 2014 NTHUOJ team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOsT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
from django.db import models
from user.models import User
from group.models import Group
from contest.models import Contest
from problem.models import Problem
from general_tools.log import get_logger

logger = get_logger()

#contest ownership
def has_c_ownership(curr_user, curr_contest):
    user_is_valid(curr_user) #check user
    #check contset
    try:
        Contest.objects.get(id=curr_contest.id)
    except Contest.DoesNotExist:
        logger.warning('Contest id %ld does not exsit!' % curr_contest.id)

    ownership = (curr_user.username == curr_contest.owner)
    if curr_contest.coowner.all().count() != 0:
        for coowner in curr_contest.coowner.all():
            if curr_user == coowner:
                ownership = True
    return ownership

#group ownership
def has_g_ownership(curr_user, curr_group):
    user_is_valid(curr_user) #check user
    #check group
    try:
        Group.objects.get(id=curr_group.id)
    except Group.DoesNotExist:
        logger.warning('Group id %ld does not exsit!' % curr_group.id)

    ownership = (curr_user.username == curr_group.owner)
    if curr_group.coowner.all().count() != 0:
        for coowner in curr_group.coowner.all():
            if curr_user == coowner:
                ownership = True
    return ownership

#problem ownership
def has_p_ownership(curr_user, curr_problem):
    user_is_valid(curr_user) #check user
    #check problem
    try:
        Problem.objects.get(id=curr_problem.id)
    except Problem.DoesNotExist:
        logger.warning('Problem id %ld does not exsit!' % curr_problem.id)

    ownership = (curr_user.username == curr_problem.owner)
    return ownership

def user_is_valid(curr_user):
    try:
        User.objects.get(username=curr_user.username)
    except User.DoesNotExist:
        logger.warning('User username %s does not exsit!' % curr_user.username)
