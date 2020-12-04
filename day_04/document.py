import re


class Document:
    REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    VALID_ECL = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def __init__(self, elements):
        self.elements = elements

    def has_all_fields(self):
        """
        Checks if all required fields are present
        """
        return len(self.REQUIRED_FIELDS - set(self.elements.keys())) == 0

    def all_fields_valid(self):
        """
        Validates all required fields
        """
        return all(
            (
                self.validate_byr(),
                self.validate_iyr(),
                self.validate_eyr(),
                self.validate_hgt(),
                self.validate_hcl(),
                self.validate_ecl(),
                self.validate_pid(),
            )
        )

    @staticmethod
    def _validate_number(number, min_, max_):
        """
        Checks if the required number is a valid number and is in the interval [min_, max_]
        """
        try:
            return min_ <= int(number) <= max_
        except ValueError:
            return False

    def validate_byr(self):
        """
        Validates the Birth Year
        """
        return self._validate_number(self.elements["byr"], 1920, 2002)

    def validate_iyr(self):
        """
        Validates the Issue Year
        """
        return self._validate_number(self.elements["iyr"], 2010, 2020)

    def validate_eyr(self):
        """
        Validates the Expiration Year
        """
        return self._validate_number(self.elements["eyr"], 2020, 2030)

    def validate_hgt(self):
        """
        Validates the Height
        """
        if (unit := self.elements["hgt"][-2:]) == "cm":
            return self._validate_number(self.elements["hgt"][:-2], 150, 193)
        elif unit == "in":
            return self._validate_number(self.elements["hgt"][:-2], 59, 76)
        return False

    def validate_hcl(self):
        """
        Validates the Hair Color
        """
        return re.search(r"^#[0-9a-f]{6}$", self.elements["hcl"])

    def validate_ecl(self):
        """
        Validates the Eye Color
        """
        return self.elements["ecl"] in self.VALID_ECL

    def validate_pid(self):
        """
        Validates the Passport ID
        """
        return re.search(r"^[0-9]{9}$", self.elements["pid"])
