#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutAsserts(Koan):

    def test_assert_truth(self):
        """
        We shall contemplate truth by testing reality, via asserts.
        """

        # Confused? This video should help:
        #
        #   http://bit.ly/about_asserts

        self.assertTrue(False) # This should be True

    def test_fill_in_values(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertEqual(__, 1 + 1)

    def test_assert_not_equal_values(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertNotEqual(__, 1 + 1)

    def test_assert_equality(self):
        """
        To understand reality, we must compare our expectations against reality.
        """
        expected_value = __
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)

    def test_a_better_way_of_asserting_equality(self):
        """
        Some ways of asserting equality are better than others.
        """
        expected_value = __
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)
