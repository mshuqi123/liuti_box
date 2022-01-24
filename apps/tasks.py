#!/usr/bin/python
# -*- coding: UTF-8 -*-
from celery import shared_task


@shared_task
def add(x, y):
    print("task----------1111111111111111111111")
    return x + y


@shared_task
def mul(x, y):
    return x * y




