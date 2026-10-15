"""wabit fork: a plugin tile of a media player gets its cover's address whole, and the app may fetch it."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'screen_manager' / 'app'))

import plugin_pictures  # noqa: E402
import plugins  # noqa: E402

PROXY = ('/api/media_player_proxy/media_player.bathroom?token=44d2467aa63ee7229a9625c436086491612f9cbd281fe3223bdadf'
         '4288b173d2&cache=9f985a3b2220be9e')
TILE = {'pictures': 1, 'domains': ['media_player']}
MANIFEST = {'permissions': {'network': []}}


class PictureAddress(unittest.TestCase):
    def test_a_players_cover_goes_whole_without_its_token(self):
        self.assertEqual(plugins.picture_address(PROXY), '/api/media_player_proxy/media_player.bathroom?cache=9f985a3b2220be9e')

    def test_other_pictures_go_as_they_are(self):
        self.assertEqual(plugins.picture_address('/api/image/serve/abc123/512x512'), '/api/image/serve/abc123/512x512')

    def test_an_address_past_512_bytes_goes_as_none(self):
        self.assertEqual(plugins.picture_address('/local/' + 'a' * 600), '')


class Allowed(unittest.TestCase):
    def test_a_players_cover_is_home_assistants_own(self):
        self.assertEqual(plugin_pictures.allowed(plugins.picture_address(PROXY), MANIFEST, TILE), 'home_assistant')

    def test_not_for_a_tile_without_an_entity(self):
        self.assertIsNone(plugin_pictures.allowed(PROXY, MANIFEST, {'pictures': 1}))

    def test_nothing_else_under_the_proxy(self):
        self.assertIsNone(plugin_pictures.allowed('/api/media_player_proxy/camera.door', MANIFEST, TILE))


if __name__ == '__main__':
    unittest.main()
