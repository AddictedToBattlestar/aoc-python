from unittest import TestCase

from day5_seed_fertilizer.seeding_location_mapper import SeedingLocationMapper, SeedingMap, SeedingCategoryProcessor, \
    calculate_from_file, find_seed_numbers


class TestLocationMap(TestCase):
    def test_get_destination_location1(self):
        subject = SeedingMap("50 98 2")
        self.assertEqual(98, subject.min)
        self.assertEqual(99, subject.max)
        self.assertEqual(-48, subject.offset)

    def test_get_destination_location2(self):
        subject = SeedingMap("52 50 48")
        self.assertEqual(50, subject.min)
        self.assertEqual(97, subject.max)
        self.assertEqual(2, subject.offset)


class TestSeedingLocationMapper(TestCase):
    def test_get_destination_location(self):
        mapper = SeedingLocationMapper([
            "50 98 2",
            "52 50 48"
        ])
        self.assertEqual(0, mapper.get_destination_location(0))
        self.assertEqual(1, mapper.get_destination_location(1))
        self.assertEqual(48, mapper.get_destination_location(48))
        self.assertEqual(49, mapper.get_destination_location(49))
        self.assertEqual(52, mapper.get_destination_location(50))
        self.assertEqual(53, mapper.get_destination_location(51))
        self.assertEqual(98, mapper.get_destination_location(96))
        self.assertEqual(99, mapper.get_destination_location(97))
        self.assertEqual(50, mapper.get_destination_location(98))
        self.assertEqual(51, mapper.get_destination_location(99))


class TestSeedingCategoryProcessor(TestCase):
    def test_find_location_number(self):
        subject = setup_seeding_category_processor_data()

        self.assertEqual(82, subject.find_location_number(79))
        self.assertEqual(43, subject.find_location_number(14))
        self.assertEqual(86, subject.find_location_number(55))
        self.assertEqual(35, subject.find_location_number(13))

    def test_find_lowest_location_number(self):
        subject = setup_seeding_category_processor_data()
        self.assertEqual(35, subject.find_lowest_location_number("79 14 55 13"))

    def test_calculate_from_file(self):
        self.assertEqual(35, calculate_from_file("../day5_seed_fertilizer/day5_sample_data.txt"))

    def test_find_lowest_location_number_using_seed_number_revisions(self):
        subject = setup_seeding_category_processor_data()
        self.assertEqual(46, subject.find_lowest_location_number(raw_seed_numbers="79 14 55 13", use_revised_seeding_map=True))

    def test_calculate_from_file_using_seed_number_revisions(self):
        self.assertEqual(46, calculate_from_file(file_name="../day5_seed_fertilizer/day5_sample_data.txt",
                                                 use_revised_seeding_map=True))


def setup_seeding_category_processor_data():
    seed_to_soil_mapper = SeedingLocationMapper([
        "50 98 2",
        "52 50 48"
    ])
    soil_to_fertilizer_mapper = SeedingLocationMapper([
        "0 15 37",
        "37 52 2",
        "39 0 15"
    ])
    fertilizer_to_water_mapper = SeedingLocationMapper([
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4"
    ])
    water_to_light_mapper = SeedingLocationMapper([
        "88 18 7",
        "18 25 70"
    ])
    light_to_temperature_mapper = SeedingLocationMapper([
        "45 77 23",
        "81 45 19",
        "68 64 13"
    ])
    temperature_to_humidity_mapper = SeedingLocationMapper([
        "0 69 1",
        "1 0 69"
    ])
    humidity_to_location_mapper = SeedingLocationMapper([
        "60 56 37",
        "56 93 4"
    ])
    seeding_mappers = [
        seed_to_soil_mapper,
        soil_to_fertilizer_mapper,
        fertilizer_to_water_mapper,
        water_to_light_mapper,
        light_to_temperature_mapper,
        temperature_to_humidity_mapper,
        humidity_to_location_mapper
    ]
    subject = SeedingCategoryProcessor(seeding_mappers)
    return subject


class Test(TestCase):
    def test_find_seed_numbers(self):
        self.assertEqual([79, 14, 55, 13], find_seed_numbers("79 14 55 13"))

    def test_find_seed_numbers_using_range(self):
        self.assertEqual([79,80,81,82,83,84,85,86,87,88,89,90,91,92,55,56,57,58,59,60,61,62,63,64,65,66,67],
                         find_seed_numbers(raw_seed_numbers="79 14 55 13", use_revised_seeding_map=True))
