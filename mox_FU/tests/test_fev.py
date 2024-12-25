

def test_favorites(fev_contract):
    #fev_contract = deploy_fav()

    assert fev_contract.retrieve() == 75

def test_can_change_value(fev_contract):
    # Arrange
    #fev_contract = deploy_fav()
    #Act
    fev_contract.store(100)
    # Assert
    assert fev_contract.retrieve() == 100

def test_can_add_people(fev_contract):
    # Arrange
    #fev_contract = deploy_fav()
    # Act
    fev_contract.add_person("John Doe", 45)
    # Assert
    stored_person = fev_contract.list_of_people(0)  # Get the first person in the array
    assert stored_person[1] == "John Doe"  # Check the name
    assert stored_person[0] == 45  # Check the favorite number
   
