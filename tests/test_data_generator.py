from db.data_generator import FIRST_NAMES, GROUPS_IDS, LAST_NAMES, Generator


def test_generate_200_names():
    result = Generator().generate_200_unique_students_names()
    assert len(result) == 200
    for name in result:
        assert len(name.split()) == 2
        assert name.split()[0] in FIRST_NAMES
        assert name.split()[1] in LAST_NAMES


def test_create_groups():
    result = Generator().generate_groups()
    for group_name in result:
        assert group_name.split("_")[0].isalpha()
        assert group_name.split("_")[1].isdigit()
    assert len(result) == 10


def test_divide_students_into_groups():
    result = Generator().divide_students_into_groups()
    for group_id in result:
        assert group_id in GROUPS_IDS
    assert len(result) == 200


def test_divide_students_into_courses():
    result = Generator().divide_students_into_courses()
    for student_course in result:
        list_of_values = student_course.values()
        assert list(list_of_values)[0] in range(1, 201)
        assert list(list_of_values)[1] in range(1, 11)
        assert "student_id" in student_course.keys()
        assert "course_id" in student_course.keys()
