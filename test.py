from gomoku.env import GomokuEnv, Action


env = GomokuEnv(size=15, player_1_name='a', player_2_name='b')
env.reset()


def test_check_done():
    # horizontal
    action = Action(0, 0, 'w')
    _, _, done, info = env.step('a', action)
    assert not done  
    action = Action(0, 1, 'w')
    _, _, done, info = env.step('a', action)
    assert not done    
    action = Action(0, 2, 'w')
    _, _, done, info = env.step('a', action)
    assert not done    
    action = Action(0, 3, 'w')
    _, _, done, info = env.step('a', action)
    assert not done    
    action = Action(0, 4, 'w')
    _, _, done, info = env.step('a', action)
    assert done and 'horizontal' in info    

    env.reset()

    # vertical
    action = Action(0, 0, 'w')
    _, _, done, info = env.step('a', action)
    assert not done  
    action = Action(1, 0, 'w')
    _, _, done, info = env.step('a', action)
    assert not done
    action = Action(2, 0, 'w')
    _, _, done, info = env.step('a', action)
    assert not done    
    action = Action(3, 0, 'w')
    _, _, done, info = env.step('a', action)
    assert not done
    action = Action(4, 0, 'w')
    _, _, done, info = env.step('a', action)
    assert done and 'vertical' in info
    # env.render()

    env.reset()
    
    # left_diagonal
    action = Action(0, 0, 'w')
    _, _, done, info = env.step('a', action)
    assert not done
    action = Action(1, 1, 'w')
    _, _, done, info = env.step('a', action)
    assert not done
    action = Action(2, 2, 'w')
    _, _, done, info = env.step('a', action)
    assert not done
    action = Action(3, 3, 'w')
    _, _, done, info = env.step('a', action)
    assert not done
    action = Action(4, 4, 'w')
    _, _, done, info = env.step('a', action)
    assert done and 'left_diagonal' in info

    env.reset()

    # right_diagonal
    action = Action(14, 0, 'w')
    _, _, done, info = env.step('a', action)
    assert not done
    action = Action(13, 1, 'w')
    _, _, done, info = env.step('a', action)
    assert not done
    action = Action(12, 2, 'w')
    _, _, done, info = env.step('a', action)
    assert not done
    action = Action(11, 3, 'w')
    _, _, done, info = env.step('a', action)
    assert not done
    action = Action(10, 4, 'w')
    _, _, done, info = env.step('a', action)
    assert done and 'right_diagonal' in info

    env.reset()

    for i in range(env.board.n):
        for j in range(env.board.n):
            action = Action(i, j, 'b')
            _, _, done, info = env.step('a', action)

    assert done and 'draw' in info 


def main():
    test_check_done()


if __name__ == '__main__':
    main()
