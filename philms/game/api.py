from game.models import Game, Player


def close_game(player: Player):
    game = player.game
    if player.is_owner:
        game.is_open = False
        game.save()
    return game


def add_player(player_name: str, game: Game, is_owner: bool = False):
    if game.is_open:
        return Player.objects.create(
            name=player_name, game=game, is_owner=is_owner)


def create_game(player_name):
    game = Game.objects.create()
    player = Player.objects.create(name=player_name, game=game, is_owner=True)
