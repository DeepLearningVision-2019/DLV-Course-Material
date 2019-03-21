import gym

env = gym.make('CartPole-v0')
env.reset()
try:
    for i in range(500):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            env.reset()
finally:
    env.close()