import random


class Queue:
    """A FIFO queue used to model a customer raffle."""

    def __init__(self):
        self.items = []  # front of the queue is index 0

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item, or None if the queue is empty."""
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        """Return the front item without removing it, or None if empty."""
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """Pick a random winner, dequeue everyone up to and including them
        (FIFO order), print the result, and return the winner."""
        if self.is_empty():
            print("No entries in the raffle.")
            return None

        # Position of the winner in the queue (0 = front)
        winner_index = random.randint(0, len(self.items) - 1)

        # Dequeue winner_index + 1 times so the winner is removed too
        removed = []
        for _ in range(winner_index + 1):
            removed.append(self.dequeue())

        winner = removed[-1]
        print(f"Winner: {winner} (position {winner_index + 1})")
        print(f"Removed from queue: {removed}")
        print(f"Remaining in queue: {len(self.items)}")
        return winner