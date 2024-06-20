def test_distribucion_equilibrada():
    # Test case with equal number of votes and seats
    assert asignar_bancas([1000, 1000, 1000], 3, 3000) == [1, 1, 1]

    # Test case with more votes than seats
    assert asignar_bancas([2000, 2000, 2000], 3, 5000) == [2, 2, 2]

    # Test case with fewer votes than seats
    assert asignar_bancas([500, 500, 500], 3, 2000) == [0, 0, 0]

    # Test case with zero votes
    assert asignar_bancas([0, 0, 0], 3, 0) == [0, 0, 0]