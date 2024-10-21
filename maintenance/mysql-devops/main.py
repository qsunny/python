from com.yunlang.backup import backup, clean

if __name__ == "__main__":
    try:
        backup()
    finally:
        clean()