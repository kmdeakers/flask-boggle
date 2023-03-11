from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure correct HTML is rendered and displayed"""

        with self.client as client:
            response = client.get('/')

            # test that you're getting a template
            html = response.get_data(as_text = True)

            #considered whole line for check, but considered if class name changes
            #our code would have to be updated... mixing front end and backend EEK
            #BUT if someone adds many tables???? which outweighs here
            #can do ID or string to make sure it is the correct doc as well
            self.assertIn('id="board-table"', html)
            self.assertEqual(response.status_code, 200)

    def test_api_new_game(self):
        """Test starting a new game."""
        # write a test for this route
        with self.client as client:
            response = client.post('/api/new-game')
            game_data = response.get_json()
            game_board = game_data['board']
            game_id = game_data['gameId']

            # checks is board is a list
            self.assertTrue(isinstance(game_board, list))
            # check is board is list of list
            self.assertTrue(isinstance(game_board[0], list))
            # check if game_id is string
            self.assertTrue(isinstance(game_id, str))
            #check if current game is in games dictionary
            self.assertIn(game_id, games, "id not in games")


