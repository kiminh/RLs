dqn_config = {
    'lr': 5.0e-4,
    'gamma': 0.99,
    'epsilon': 0.2,
    'max_episode': 50000,
    'batch_size': 1024,
    'buffer_size': 200000,
    'assign_interval': 1000,
    'use_priority': False,
    'n_step': False
}
ddqn_config = {
    'lr': 5.0e-4,
    'gamma': 0.99,
    'epsilon': 0.2,
    'max_episode': 50000,
    'batch_size': 1024,
    'buffer_size': 200000,
    'assign_interval': 1000,
    'use_priority': False,
    'n_step': False
}
dddqn_config = {
    'lr': 5.0e-4,
    'gamma': 0.99,
    'epsilon': 0.2,
    'max_episode': 50000,
    'batch_size': 1024,
    'buffer_size': 200000,
    'assign_interval': 1000,
    'use_priority': False,
    'n_step': False
}
pg_config = {
    'epsilon': 0.2,
    'lr': 5.0e-4,
    'gamma': 0.99,
    'max_episode': 50000,
    'batch_size': 1024,
    'epoch': 1  # very important
}
ac_config = {
    'lr': 5.0e-4,
    'epsilon': 0.2,
    'gamma': 0.99,
    'max_episode': 50000,
    'batch_size': 1024,
    'buffer_size': 200000,
    'use_priority': False,
    'n_step': False
}
a2c_config = {
    'epsilon': 0.2,
    'lr': 5.0e-4,
    'gamma': 0.99,
    'beta': 1.0e-3,
    'max_episode': 50000,
    'batch_size': 1024,
    'epoch': 4,  # very important
    'sample_count': 1,  # 采样的次数
}
ppo_config = {
    'epsilon': 0.2,
    'gamma': 0.99,
    'beta': 1.0e-3,
    'lr': 5.0e-4,
    'lambda_': 0.97,
    'max_episode': 50000,
    'batch_size': 1024,
    'sample_count': 1,  # 采样的次数
    'epoch': 1,  # very important
    'share_net': True,

    'actor_lr': 3e-4,
    'critic_lr': 1e-3,
    'actor_epoch': 4,
    'critic_epoch': 4,
}
dpg_config = {
    'gamma': 0.99,
    'lr': 5.0e-4,
    'discrete_tau': 1.0,
    'max_episode': 50000,
    'batch_size': 1024,
    'buffer_size': 200000,
    'use_priority': False,
    'n_step': False
}
ddpg_config = {
    'gamma': 0.99,
    'ployak': 0.995,
    'lr': 5.0e-4,
    'discrete_tau': 1.0,
    'max_episode': 50000,
    'batch_size': 1024,
    'buffer_size': 200000,
    'use_priority': False,
    'n_step': False
}
td3_config = {
    'gamma': 0.99,
    'ployak': 0.995,
    'lr': 5.0e-4,
    'max_episode': 50000,
    'discrete_tau': 1.0, # discrete_tau越小，gumbel采样的越接近one_hot，但相应的梯度也越小
    'batch_size': 1024,
    'buffer_size': 200000,
    'use_priority': False,
    'n_step': False
}
sac_config = {
    'alpha': 0.2,
    'auto_adaption': True,
    'gamma': 0.99,
    'ployak': 0.995,
    'lr': 5.0e-4,
    'discrete_tau': 1.0,
    'max_episode': 50000,
    'batch_size': 1024,
    'buffer_size': 200000,
    'use_priority': False,
    'n_step': False
}
sac_no_v_config = {
    'alpha': 0.2,
    'auto_adaption': True,
    'lr': 5.0e-4,
    'max_episode': 50000,
    'gamma': 0.99,
    'ployak': 0.995,
    'discrete_tau': 1.0,
    'batch_size': 1024,
    'buffer_size': 200000,
    'use_priority': False,
    'n_step': False
}
maxsqn_config = {
    'alpha': 0.2,
    'epsilon': 0.2,
    'use_epsilon': False,
    'auto_adaption': True,
    'lr': 5.0e-4,
    'max_episode': 50000,
    'gamma': 0.99,
    'ployak': 0.995,
    'batch_size': 1024,
    'buffer_size': 200000,
    'use_priority': False,
    'n_step': False
}
ma_dpg_config = {
    'gamma': 0.99,
    'lr': 5.0e-4,
    'max_episode': 50000
}
ma_ddpg_config = {
    'gamma': 0.99,
    'ployak': 0.995,
    'lr': 5.0e-4,
    'max_episode': 50000
}
ma_td3_config = {
    'gamma': 0.99,
    'ployak': 0.995,
    'lr': 5.0e-4,
    'max_episode': 50000
}