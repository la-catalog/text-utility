from pathlib import Path
from unittest import TestCase, main

from text_utility import find_gtins


class TestFindGtins(TestCase):
    def setUp(self) -> None:
        self._dir = "tests/res/find_gtins"

    def test_not_raising_error(self):
        for file in Path(self._dir).iterdir():
            for gtin in find_gtins(file.read_text()):
                assert gtin.strip() != ""

    def test_find_gtins(self):
        """
        Filenames must end with a suffix that tell how many GTINs expect
        from that file. For example, file "xxxx.9" expect 9 GTINs.

        There is no easy way to test finding the correct number, someone must
        count before.
        """

        for file in Path(self._dir).iterdir():
            gtins = list(find_gtins(file.read_text()))
            expected = file.suffix[1:]

            assert len(gtins) == int(expected)


if __name__ == "__main__":
    main()
