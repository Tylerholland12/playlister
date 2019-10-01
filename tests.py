from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId




sample_playlist_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_playlist = {
    'title': 'Cat Videos',
    'description': 'Cats acting weird',
    'videos': [
        'https://youtube.com/embed/hY7m5jjJ9mM',
        'https://www.youtube.com/embed/CQ85sUNBK7w'
    ]
}
sample_form_data = {
    'title': sample_playlist['title'],
    'description': sample_playlist['description'],
    'videos': '\n'.join(sample_playlist['videos'])
}

class PlaylistsTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):
        """Test the playlists homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Playlist', result.data)

    def test_new(self):
        """Test the new playlist creation page."""
        result = self.client.get('/playlists/new')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'New Playlist', result.data)


    @mock.patch('pymongo.collection.Collection.find_one')
    def test_edit_playlist(self, mock_find):
        """Test editing a single playlist."""
        mock_find.return_value = sample_playlist

        result = self.client.get(f'/playlists/{sample_playlist_id}/edit')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Cat Videos', result.data)

if __name__ == '__main__':
    unittest_main()