import aiohttp
import asyncio
import requests

async def main():
    # 创建一个CelientSession对象命名为session
    async with aiohttp.ClientSession() as session:
        url = 'http://baidu.com'
        # 通过session的get方法得到一个ClientResponse对象，命名为resp
        async with session.get(url) as response:
            print(response.status)
if __name__ == '__main__':
    main()
    tasks = [asyncio.ensure_future(main()) for _ in range(5)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))