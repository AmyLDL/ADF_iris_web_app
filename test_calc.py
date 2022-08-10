from calc import predict_species

def test_zero ():
    # Arrange
    sepal_length = 0
    sepal_width = 0
    petal_length = 0
    petal_width = 0
    expected_species = "non predicted"

    # Act
    final_species = predict_species(sepal_length, sepal_width, petal_length, petal_width)

    # Assert
    assert final_species == expected_species


def test_Zero_outofrange ():
    # Arrange
    sepal_length = 2.0
    sepal_width = 1.5
    petal_length = 0.5
    petal_width = 3.0
    expected_species = "non predicted"

    # Act
    final_species = predict_species(sepal_length, sepal_width, petal_length, petal_width)

    # Assert
    assert final_species == expected_species

def test_setosa ():
    # Arrange
    sepal_length = 5.1
    sepal_width = 3.5
    petal_length = 1.4
    petal_width = 0.2
    expected_species = "setosa"

    # Act
    final_species = predict_species(sepal_length, sepal_width, petal_length, petal_width)

    # Assert
    assert final_species == expected_species

def test_versicolor ():
    # Arrange
    sepal_length = 5.7
    sepal_width = 2.8
    petal_length = 4.5
    petal_width = 1.3
    expected_species = "versicolor"

    # Act
    final_species = predict_species(sepal_length, sepal_width, petal_length, petal_width)

    # Assert
    assert final_species == expected_species

def test_virginica ():
    # Arrange
    sepal_length = 6.7
    sepal_width = 2.5
    petal_length = 5.8
    petal_width = 1.8
    expected_species = "virginica"

    # Act
    final_species = predict_species(sepal_length, sepal_width, petal_length, petal_width)

    # Assert
    assert final_species == expected_species