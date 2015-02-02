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
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
def get_running_contest(request):
        all_running_contest_list = [
            {'name':'contest', 'time':'20111010'},
            {'name':'contest', 'time':'20140505'},
            {'name':'contest', 'time':'20122222'},
            {'name':'contest', 'time':'20133333'},
            {'name':'contest', 'time':'20144444'},
            {'name':'contest', 'time':'20166666'},
            {'name':'contest', 'time':'20122222'},
            {'name':'contest', 'time':'20133333'},
            {'name':'contest', 'time':'20144444'},
            {'name':'contest', 'time':'20166666'},
            {'name':'contest', 'time':'20122222'},
            {'name':'contest', 'time':'20133333'},
            {'name':'contest', 'time':'20144444'},
            {'name':'contest', 'time':'20166666'},
            {'name':'contest', 'time':'20177777'}
        ] 
        return render(
            request, 'group/viewall.html', {
                'C_data': all_running_contest_list, 
                'title': 'running contest',
            })

def get_ended_contest(request):
        all_ended_contest_list = [
            {'name':'archive', 'time':'20111010'},
            {'name':'archive', 'time':'20140505'},
            {'name':'archive', 'time':'20122222'},
            {'name':'archive', 'time':'20133333'},
            {'name':'archive', 'time':'20144444'},
            {'name':'archive', 'time':'20166666'},
            {'name':'archive', 'time':'20111010'},
            {'name':'archive', 'time':'20140505'},
            {'name':'archive', 'time':'20122222'},
            {'name':'archive', 'time':'20133333'},
            {'name':'archive', 'time':'20144444'},
            {'name':'archive', 'time':'20166666'},
        ] 
        return render(
            request, 'group/viewall.html', {
                'C_data': all_ended_contest_list, 
                'title': 'ended contest',
            })

def get_all_announce(request):
        all_announce_list = [
            {'name':'announce', 'time':'20111010'},
            {'name':'announce', 'time':'20140505'},
            {'name':'announce', 'time':'20122222'},
            {'name':'announce', 'time':'20133333'},
            {'name':'announce', 'time':'20144444'},
            {'name':'announce', 'time':'20166666'},
            {'name':'announce', 'time':'20122222'},
            {'name':'announce', 'time':'20111010'},
            {'name':'announce', 'time':'20140505'},
            {'name':'announce', 'time':'20122222'},
            {'name':'announce', 'time':'20133333'},
            {'name':'announce', 'time':'20144444'},
            {'name':'announce', 'time':'20166666'},
            {'name':'announce', 'time':'20122222'},
        ] 
        return render(
            request, 'group/viewall.html', {
                'C_data': all_announce_list, 
                'title': 'announce',
            })

    
def detail(request,group_id):
    running_contest_list = [
        {'name':'11111', 'time':'20111010'},
        {'name':'22222', 'time':'20140505'},
        {'name':'33333', 'time':'20122222'},
        {'name':'44444', 'time':'20133333'},
        {'name':'55555', 'time':'20144444'},
    ]

    ended_contest_list = [
        {'name':'aaaaa', 'time':'20111010'},
        {'name':'bbbbb', 'time':'20140505'},
        {'name':'ccccc', 'time':'20122222'},
        {'name':'ddddd', 'time':'20133333'},
        {'name':'eeeee', 'time':'20144444'},
    ]

    annowence_list = [
        {'name':'annowence_1','op':'drowsy', 'time':'20111010'},
        {'name':'annowence_2','op':'drowsy', 'time':'20140505'},
    ]

    student_list =[
        {'name': 'Tom', 'time': '2014/1/2 23:00'},
        {'name': 'Amy', 'time': '2014/1/2 23:00'},
        {'name': 'Jess', 'time': '2014/1/2 23:00'},
        {'name': 'Bieber', 'time': '2014/1/2 23:00'},
        {'name': 'Ian', 'time': '2014/1/2 23:00'},
        {'name': 'Anthony', 'time': '2014/1/2 23:00'},
        {'name': 'Lily', 'time': '2014/1/2 23:00'}
    ]

    ta_list =[
        {'name': 'drowsy'},
        {'name': 'henry'},
    ]

    return render(
        request, 'group/groupDetail.html', {
            'rc_list': running_contest_list, 
            'ec_list': ended_contest_list,
            'an_list': annowence_list,
            'ta_list': ta_list,
            's_list': student_list,
            'group_name': 'GGgroup', 
            'group_description': 'blablabla, this is a description',
        })


def list(request):
    group_data = [
        {'name': 'GGgroup', 'ta_name': 'drowsy, henry', 'mem_number': '42', 'gid': '001'},
        {'name': '2ndgroup', 'ta_name': 'TA1', 'mem_number': '1', 'gid': '002'},
        {'name': '3rdgroup', 'ta_name': 'TA2, henry', 'mem_number': '22', 'gid': '003'},
        {'name': '4thgroup', 'ta_name': 'drowsy, TA3', 'mem_number': '34', 'gid': '004'},
        {'name': '5thgroup', 'ta_name': 'TA4', 'mem_number': '105', 'gid': '005'},
        {'name': '6thgroup', 'ta_name': 'T5A', 'mem_number': '42', 'gid': '006'}
    ]
    return render(
        request,'group/groupList.html', {
            'G_data': group_data
        })
