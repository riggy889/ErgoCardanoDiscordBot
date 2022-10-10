import time
import rabbit

safety_delay = 5
delay = 2 + safety_delay
refresh_delay = 30

# Getting initial state of sales
rabbitDetailsData = rabbit.GetLatestRabbitSales() # Gets details for all current rabits that've sold
exisitingRabbitTxns = rabbit.BuildExistingTxnList(rabbitDetailsData) # Puts exisitng txns into list

#Bot loop
while True:
    try:
        print('Searching API Now...')
        rabbitDetailsData = rabbit.GetLatestRabbitSales()
        time.sleep(refresh_delay)
    except:
        print('Didnt work...')

    #Checking all activities (by signature, key values)
    for activity in rabbitDetailsData:
        #Checking if there is a new activity
        if activity['tx_hash'] not in exisitingRabbitTxns:
            try:
                rabbitString = rabbit.build_rabbit_string(activity)
                time.sleep(delay)
            except:
                print("Error!")

    print('End of loop...')
    exisitingRabbitTxns = rabbit.BuildExistingTxnList(rabbitDetailsData)
