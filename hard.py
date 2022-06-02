#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b = 'процессор', 'информация'

print(*[i for i in a if not i in b] + [i for i in b if not i in a], sep=' ')