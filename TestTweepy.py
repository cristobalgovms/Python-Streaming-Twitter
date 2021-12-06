import tweepy
import psycopg2
import json

crypto_tickers = ['#PancakeSwap']
consumer_key = '2BrwPf9bjVymsad9ZEstL3r10'
consumer_secret = 'gdTN2S1ZnZk2EUIeIt6P5vlNNA6MzqDayZiUX9xSi8gjhU1jEs'
access_token = '4046278457-Ds9OyG1kt5bVnhKnThwPqyCIOl7EsEu3LyrKoaK'
access_token_secret = 'YUX2WBLfLxZ2dRa4rWr7wYlKvMCQu9eGc3rRBEn2NFwvf'
myConnection = psycopg2.connect(host='localhost', user='postgres', password='Skyliner34', dbname='postgres')


class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        try:
            cur = myConnection.cursor()
            query_sql = """INSERT INTO public.tweets(data) VALUES (%s);"""
            cur.execute(query_sql, (json.dumps(status._json),))
            myConnection.commit()

            return True

        except BaseException as e:
            print("Error en el on_data: %s" % str(e))

def sendData():
    printer = IDPrinter(consumer_key, consumer_secret,access_token, access_token_secret)
    printer.filter(track=crypto_tickers)

if __name__ == "__main__":
    sendData()