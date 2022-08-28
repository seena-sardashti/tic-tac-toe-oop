class Move:
    def __init__(self, store, player, state):
        self.store = store
        self.player = player
        self.state = state
        self.winner = None
        move_id = len(store['moves']) + 1
        self.id = move_id
        if player:
            self.player_id = player.id
        if state:
            self.state_id = state.id
        store['moves'][self.id] = self