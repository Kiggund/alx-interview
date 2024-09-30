#!/usr/bin/python3

def isWinner(x, nums):
    def sieve(n):

        """ Helper function to generate a list of primes up to n
        using the Sieve of Eratosthenes """

        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulate the game for a given n """
        primes = sieve(n)
        moves = 0
        while primes:
            prime = primes.pop(0)
            primes = [p for p in primes if p % prime != 0]
            moves += 1
            """
            Maria wins if moves are odd,
             Benwinsif moves are even
            """
        return moves % 2 == 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
