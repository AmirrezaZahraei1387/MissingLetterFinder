import datatr.trainer as dt

trainer = dt.TrainMC("raw-data")
counter = trainer.train()

dt.writeCsv("re-data", "redata.csv", counter)