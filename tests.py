import unittest
import freemail


class TestFreemail(unittest.TestCase):

    def test_free(self):
        self.assertTrue(freemail.is_free('smith@gmail.com'))
        self.assertTrue(freemail.is_free('jack@mailinater.com'))
        self.assertFalse(freemail.is_free('something@notfree.com'))

    def test_disposable(self):
        self.assertFalse(freemail.is_disposable('smith@gmail.com'))
        self.assertTrue(freemail.is_disposable('jack@mailinater.com'))

if __name__ == '__main__':
    unittest.main()
