#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: exceptions.py

class AuthFailed(Exception):
    """Authentication failed. Invalid token or host url"""
