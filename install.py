#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os;
import sys;
import errno;
import shutil;
import subprocess;

# 全局变量声明
HOME     = os.environ['HOME'];
VIM_PATH = HOME + '/.fevim';
APP_NAME = 'fevim';
REQUIRE  = ['npm', 'node', 'git'];
GIT_URL  = 'https://github.com/yuanzm/fe-vim.git';

# 打印关键信息
def msg(message):
    print message;

# 执行成功日志
def success(str1, str2 = ''):
    msg ("\33[32m ✔ \33[0m %s %s" % (str1, str2));

# 打印错误日志
def error(str1, str2 = ''):
    msg ("\33[32m ✘ \33[0m %s %s" % (str1, str2));

# 打印warning日志
def warn(str1, str2 = ''):
    msg ("\33[32m ⚠ \33[0m %s %s" % (str1, str2));

# 打印提示信息
def info(str1, str2 = ''):
    msg ("\33[32m ➜ \33[0m %s %s" % (str1, str2));

# 强制创建软连接
def lnif(src, dist):
    try:
        os.symlink(src, dist);

    except OSError, e:
        if e.errno == errno.EEXIST:
            warn('link %s already exist!' %(dist));
            os.remove(dist)
            os.symlink(src, dist);

# 判断Shell命令是否存在
def checkOneCommandExist(command):
    return subprocess.call('command -v %s >/dev/null' % command, shell=True) == 0;

# 判断当前环境是否满足要求
def checkEnv():
    info('checking system environment...');

    for command in REQUIRE:
        if ( checkOneCommandExist(command) is False ):
            error( "%s not found. Please Make sure you have installed" % command)
            # 如果硬性环境不满足，直接不执行后续逻辑
            sys.exit(0);

    success('your system environment meets the requirements!');

# 将Git仓库拷贝或者更新
def initVimGitRepo():
    if os.path.exists(VIM_PATH) is False:
        os.mkdir(VIM_PATH);
        info("cloning repo fevim to %s..." % (VIM_PATH));
        command = 'git clone %s %s' % (GIT_URL, VIM_PATH)
        ret = subprocess.call(command, shell = True);

        if ret is 0:
            success('repo has been cloned successfully!');

    else:
        info('updating repo fevim %s...' % (GIT_URL));
        os.chdir(VIM_PATH);
        command = 'git pull origin master';
        ret = subprocess.call(command, shell = True);

        if ret is 0:
            success('repo has been updated successfully!');

# 设置文件软连接
def setFileLink():
    info('setting up syslinks...');

    lnif(VIM_PATH + '/vimrc', HOME + '/.vimrc');
    lnif(VIM_PATH, HOME + '/.vim');
    lnif(VIM_PATH + '/others/editorconfig', HOME + '/.editorconfigtest');

    success('setting up syslinks successfully!');

# 拷贝一些配置文件用于初始化Vim环境
def initVimEnv():
    info('start to init vim environment...');

    shutil.copyfile(HOME + '/.vim/vimrc.local.example', HOME + '/.vim/vimrc.local');
    shutil.copyfile(HOME + '/.vim/vimrc.bundles.local.example', HOME + '/.vim/vimrc.bundles.local');
    shutil.copyfile(HOME + '/.vim/vimrc.before.example', HOME + '/.vim/vimrc.before');

    success('vim environment has beed inited successfully');

# 安装Vim插件管理器
def installVimPlug():
    info('installing Vim-plug');

    ret = subprocess.call('curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim', shell = True);

    success("successfully installed vim-plug");

# 通过shell命令安装Vim插件
def installPluginsWithVimPlug():
    info('install/update plugins');

    ret = subprocess.call("vim +'PlugInstall --sync' +qall", shell = True);

    if ret is 0:
        success('all vim plugins has been installed successfully');

# 脚本主函数
def main():
    # step1 判断基本的环境要求
    checkEnv();

    # step2 拷贝本项目文件到相对应的文件夹
    initVimGitRepo();

    # step3 为Vim的配置文件创建软连接
    setFileLink();

    # 初始化Vim的一些配置
    initVimEnv();

    # 安装Vim的插件管理器
    installVimPlug();

    # 通过命令行安装Vim的插件
    installPluginsWithVimPlug();

    sys.exit(0);

if __name__ == '__main__':
    main();

