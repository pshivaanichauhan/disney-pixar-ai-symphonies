import numpy as np

class Strategy:
    def __init__(self, probs):
        self.probs = np.array(probs, dtype=float)
        self.probs /= self.probs.sum()

def payoff_matrix():
    # Calm, Build, Clash
    return np.array([[0.3,0.1,-0.2],
                     [0.1,0.4, 0.2],
                     [-0.1,0.3,0.5]])

def compute_stackelberg(iterations=2000, lr=0.05):
    A = payoff_matrix()
    leader = Strategy([0.3,0.4,0.3])
    follower = Strategy([0.33,0.33,0.34])
    for _ in range(iterations):
        # follower best response
        col_pay = leader.probs @ A
        best_f = np.argmax(col_pay)
        target_f = np.eye(3)[best_f]
        follower.probs = follower.probs*(1-lr) + target_f*lr
        # leader update
        row_pay = A @ follower.probs
        best_l = np.argmax(row_pay)
        target_l = np.eye(3)[best_l]
        leader.probs = leader.probs*(1-lr) + target_l*lr
    leader_val = leader.probs @ (A @ follower.probs)
    leader_best = float(np.max(A @ follower.probs))
    follower_val = float(leader.probs @ A @ follower.probs)
    follower_best = float(np.max(leader.probs @ A))
    regret = max(leader_best - leader_val, follower_best - follower_val)
    return type('Res', (), {'leader':leader, 'follower':follower, 'regret':float(regret)})

if __name__ == '__main__':
    res = compute_stackelberg()
    print('Leader probs:', res.leader.probs)
    print('Follower probs:', res.follower.probs)
    print('Regret:', res.regret)
