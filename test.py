# Testing script
# author: ynie
# date: April, 2020
from utils.project_utils import load_device, load_model, load_tester, load_dataloader
from utils.project_utils import CheckpointIO
from test_epoch import test
import wandb


def run(cfg):
    if wandb.run is None:
        resume = cfg.config['resume']
        name = cfg.config['name']
        id = cfg.config['log']['path'].split('/')[-1]
        config = None if resume else cfg.config
        wandb.init(project="deeppanocontext", config=config, dir=cfg.config['log']['path'],
                   name=name, id=id, resume=resume)

    '''Begin to run network.'''
    checkpoint = CheckpointIO(cfg)

    '''Load save path'''
    cfg.log_string('Data save path: %s' % (cfg.save_path))

    import os
    output_path = "/home/lmf/tmp/deep_output_path"
    if os.path.exists(output_path):
        os.remove(output_path)
    f = open(output_path, "w")
    f.write(cfg.save_path)
    f.close()

    '''Load device'''
    cfg.log_string('Loading device settings.')
    device = load_device(cfg)

    '''Load data'''
    cfg.log_string('Loading dataset.')
    test_loader = load_dataloader(cfg.config, mode='test')

    '''Load net'''
    cfg.log_string('Loading model.')
    net = load_model(cfg, device=device)
    checkpoint.register_modules(net=net)
    cfg.log_string(net)

    '''Load existing checkpoint'''
    checkpoint.parse_checkpoint()

    '''Load tester'''
    cfg.log_string('Loading tester.')
    tester = load_tester(cfg=cfg, net=net, device=device)

    '''Start to test'''
    cfg.log_string('Start to test.')
    cfg.log_string('Total number of parameters in {0:s}: {1:d}.'.format(cfg.config['method'], sum(p.numel() for p in net.parameters())))

    test(cfg=cfg, tester=tester, test_loader=test_loader)

    cfg.log_string('Testing finished.')
