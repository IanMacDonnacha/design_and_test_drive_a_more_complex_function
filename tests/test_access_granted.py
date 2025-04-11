from lib.access_granted import *

def test_access_granted_denied_with_input():
    assert access_granted("2018-04-11") == "Access denied!"

def test_access_granted_granted_with_input():
    assert access_granted("1960-10-21") == "Access granted!"

