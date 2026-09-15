# Association Activity: Pet Clinic

Create a small program that models pets visiting a veterinarian. The `Pet` and `Veterinarian` classes must remain independent, but veterinarian objects should be able to temporarily interact with pet objects by receiving them as method parameters. This follows the temporary, independent “uses-a” relationship described in the association slides. 

Requirements:

* Create a `Pet` class with at least `name`, `species`, and `health` properties.
* Create a separate `Veterinarian` class with at least a `name` property. Neither class should create or permanently store an instance of the other class.
* Give `Veterinarian` a `checkup(pet)` method that receives a `Pet` object as a parameter and displays information about that pet.
* Give `Veterinarian` a `treat(pet, amount)` method that receives a `Pet` object and increases its `health` by the given amount.
* Create at least three different `Pet` objects and have the same `Veterinarian` object perform checkups and treatments on multiple pets.

The important relationship is that the veterinarian temporarily uses each pet object without owning or permanently storing it.

---

## File Structure

```text
pet_clinic/
│
├── pet.py
├── veterinarian.py
└── main.py
```

* `pet.py`

  * Contains the `Pet` class.
  * Stores the pet's properties and any behaviour that belongs specifically to a pet.

* `veterinarian.py`

  * Contains the `Veterinarian` class.
  * Contains methods such as `checkup(pet)` and `treat(pet, amount)` that interact with `Pet` objects passed in as parameters.

* `main.py`

  * Imports the `Pet` and `Veterinarian` classes.
  * Creates the veterinarian and pet objects.
  * Demonstrates the veterinarian interacting with multiple pets.
  * All code used to run and test the finished program should be placed here.

---

## Assessment

| Assessment Item                | Criteria                                                                                                                                               |  Marks |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -----: |
| ☐ `Pet` Class                  | Creates a `Pet` class with `name`, `species`, and `health` properties.                                                                                 |      2 |
| ☐ `Veterinarian` Class         | Creates a separate `Veterinarian` class with a `name` property.                                                                                        |      2 |
| ☐ Association Between Objects  | `Pet` objects are passed into `Veterinarian` methods as parameters. The veterinarian does not create or permanently store a `Pet` object.              |      4 |
| ☐ Checkup Behaviour            | Creates a `checkup(pet)` method that uses the passed `Pet` object and displays meaningful information about that pet.                                  |      3 |
| ☐ Treatment Behaviour          | Creates a `treat(pet, amount)` method that changes the `health` of the passed `Pet` object by the specified amount.                                    |      4 |
| ☐ Multiple Object Interactions | Creates at least three different `Pet` objects and demonstrates the same `Veterinarian` object performing checkups and/or treatments on multiple pets. |      3 |
| ☐ Complete Working Program     | The program runs without errors and clearly demonstrates that changes made through the veterinarian affect the correct pet objects.                    |      2 |
|                                | **Total**                                                                                                                                              | **20** |



