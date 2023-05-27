from common import helper, logger, globle
from core.game import init
from core.game import mem
from plugins.driver import init_driver

if __name__ == '__main__':
    try:
        globle.cmd = "cmd"
        init_driver("3swg")
        logger.info("驱动加载成功", 1)
        process_id = helper.get_process_id_by_name("DNF.exe")
        if process_id == 0:
            helper.message_box("请打开dnf后运行")
            exit()

        mem.set_process_id(process_id)

        init.init_empty_addr()
        # 初始化fastcall
        init.call.init_call()
        
        logger.info("加载成功-欢迎使用", 1)
        logger.info("当前时间：{}".format(helper.get_now_date()), 1)
        init.hotkey2()
    except KeyboardInterrupt as e:
        pass
    except Exception as err:
        import sys
        import traceback

        except_type, _, except_traceback = sys.exc_info()
        errArgs = ''.join(err.args)
        logger.file(errArgs)
        logger.file(except_type)
        for i in traceback.extract_tb(except_traceback):
            logger.file(i.name)
            logger.file(i.filename)
            logger.file(str(i.lineno))
