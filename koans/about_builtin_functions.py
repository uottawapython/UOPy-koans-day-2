#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutBuiltinFunctions(Koan):


    def test_len_returns_a_integer(self):
        #>>> help(len)
        feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals',
            'fruit bats']

        self.assertEqual(__, 5)

    def test_dir_returns_a_list_of_method_of_an_object(self):
        #>>> help(dir)
        temperature = 'wheather'

        self.assertTrue(__ >= len(dir(wheather)))

    def test_max_returns_the_maximum_value_of_a_list(self):
        #>>> help(max)
        temperature = [-78, 35,20,-5,-7]

        self.assertEqual(__, max(temperature))
        self.assertEqual(__, min(temperature))

    def test_range_returns_a_list(self):
        #>>> help(range)
        #>>> range(start,<end,step)
        temperature = range(25,29)

        self.assertEqual(__, type(temperature))
        self.assertEqual(__, range(temperature))

        temperature = range(25,29,2)
        self.assertEqual(__, range(temperature))

    def test_list_returns_a_list(self):
        #>>> help(list)
        temperature = 'weather'

        self.assertEqual(__, list(temperature))

    def test_int_returns_a_int(self):
        #>>> help(int)
        temperature = False
        self.assertEqual(__, int(temperature))

        temperature = True
        self.assertEqual(__, int(temperature))

    def test_str_returns_a_str(self):
        #>>> help(str)
        temperature = 34
        self.assertEqual(__, str(temperature))
