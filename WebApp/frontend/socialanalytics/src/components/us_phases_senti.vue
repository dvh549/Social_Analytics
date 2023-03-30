<template>
<!-- Area Chart -->
    <div class="row">
        
        <div class="col-xl-4 col-lg-7" >
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Word Cloud Negative</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body" style="height:400px">
                    <div class="chart-area">
                        <img src="../assets/negative_wordcloud_phases_us.png" height="300px" style="margin:0 auto; display: block;">
                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-4 col-lg-7" >
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Word Cloud Neutral</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body" style="height:400px">
                    <div class="chart-area">
                        <img src="../assets/neutral_wordcloud_phases_us.png" height="300px" style="margin:0 auto; display: block;">

                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-4 col-lg-7" >
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Word Cloud Positive</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body" style="height:400px">
                    <div class="chart-area">
                        <!-- {{this.positiveWordsComponent}} -->
                        <img src="../assets/positive_wordcloud_phases_us.png" height="300px" style="margin:0 auto; display: block;">

                    </div>
                </div>
            </div>
        </div>

    </div>
    <div class="row" >
        <div class="col-xl-12 col-lg-12">
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Distribution of Sentiments in Tweets</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body" style="height:400px">
                    <div class="chart-area">
                         <apexchart type="bar" height="350" :options="barChartOptions" :series="bar_start"></apexchart>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="row" v-if="this.lineData[0].data!=[] && lineChartOptions.xaxis.categories!=[]">

        <div class="col-xl-12 col-lg-12">
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Sentiment of Tweets (Weekly)</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body mb-3" style="height:600px">
                    <div class="chart-area">
                       <apexchart type="line" height="500" :options="lineChartOptions" :series="lineData"></apexchart>
                    </div>
                </div>
            </div>
        </div>

    </div>
    <div class="row" >
        <div class="col-xl-12 col-lg-12">
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Analysis</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body" style="height:300px">
                    <div class="chart-area">
                        <p>
                            <strong>*Bar Graph</strong>
                            <br/>
                            Positive tweets are the highest in proportion at 44%, followed by negative tweets at 38%, and neutral tweets at 18%. However, we found unacceptance of government measures from tweets such as “Lockdowns and restrictions don’t work to stop the #coronavirus. It only hurt businesses and mental health. Only COVID vaccine will work. Hopefully it will be distributed fast to the states that experience urgent need.”. 
                            <br/>
                            <strong>*Line Chart</strong>
                            <br/>
                            We see a noticeable peak of negative tweets that surpassed the frequency of positive tweets at the final peak (during the month of December 2020) with tweets such as “COVID f**ked everything up”, which is a (slightly) extreme representation of their frustration of how Covid affected their lives.   
                            <br/>
                            <strong>*Word Cloud</strong>
                            <br/>
                            However, we can still tell that covid-related deaths were still a continual concern for Americans.  
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>


</template>

<script>
// import wordcloud from 'vue-wordcloud'
// import VueWordCloud from 'vuewordcloud';
// import wordcloud from 'vue-wordcloud'
// import Vue3WordCloud from 'vue3-word-cloud';
// import axios from "axios";

export default {
    props: {
        // positiveWordsComponent: Array,
        // negativeWordsComponent: Array,
        // neutralWordsComponent: Array
       
    },
    components: {
        
    },
    data(){
        return{
            bar_start:[{"name":'Sentiment',"data":[36,22,42]}],
            lineData:[
                {
                    "name":"Positive",
                    "data": [1,28,64,50,39,45,371,572,1836,1640,1316,1039,830,873,632,573,528,502,473,362,282,302,343,354,387,395,377,404,379,282,258,232,245,211,232,247,201,730,483,245,287,297,353,409,458,312,351,373,386,312,126]
                },
                {
                    "name":"Neutral",
                    "data": [1,51,68,30,24,37,281,449,1228,923,670,623,440,490,323,302,271,266,234,185,105,136,174,153,167,206,179,176,176,129,134,81,123,91,113,98,93,346,253,125,146,127,179,194,194,167,176,195,222,128,66]
                },
                {
                    "name":"Negative",
                    "data": [1,1,34,99,62,49,107,469,606,1427,1214,882,819,652,670,526,415,427,346,346,354,256,243,314,305,350,371,351,331,395,273,250,226,247,179,273,228,211,614,523,218,294,255,265,315,349,312,353,417,367,292]
                }
            ],
            lineChartOptions: {
                chart: {
                    type: 'line'
                    
                },
                colors: ['#00FF00', '#FFFF00', '#FF0000'],
                // dataLabels: {
                // enabled: true,
                // },
                stroke: {
                    curve: 'smooth'
                },
                
                markers: {
                size: 1
                },
                xaxis: {
                    categories: ["2020-01-20","2020-01-27","2020-02-03","2020-02-10","2020-02-17","2020-02-24","2020-03-02","2020-03-09","2020-03-16","2020-03-23","2020-03-30","2020-04-06","2020-04-13","2020-04-20","2020-04-27","2020-05-04","2020-05-11","2020-05-18","2020-05-25","2020-06-01","2020-06-08","2020-06-15","2020-06-22","2020-06-29","2020-07-06","2020-07-13","2020-07-20","2020-07-27","2020-08-03","2020-08-10","2020-08-17","2020-08-24","2020-08-31","2020-09-07","2020-09-14","2020-09-21","2020-09-28","2020-10-05","2020-10-12","2020-10-19","2020-10-26","2020-11-02","2020-11-09","2020-11-16","2020-11-23","2020-11-30","2020-12-07","2020-12-14","2020-12-21","2020-12-28","2021-01-04"],
                    title: {
                        text: 'Date'
                    }
                },
                legend: {
                position: 'top',
                horizontalAlign: 'right',
                floating: true,
                offsetY: -25,
                offsetX: -5
                }
            },
            barChartOptions: {
                chart: {
                type: 'bar',
                },
                plotOptions: {
                bar: {
                    distributed: true,
                    horizontal: false,
                    columnWidth: '55%',
                    endingShape: 'rounded'
                },
                },
                colors: ['#00FF00', '#FFFF00', '#FF0000'],
                dataLabels: {
                enabled: false
                },
                stroke: {
                show: true,
                width: 2,
                colors: ['transparent']
                },
                xaxis: {
                categories: ['Positive',"Neutral", "Negative"],
                },
                fill: {
                opacity: 1
                }
            }  
        }
  }, 
    // async mounted(){
    //     await axios.get("http://127.0.0.1:5000/getSentimentAnalysisPhasesUS")
    //         .then(res=>{
    //         console.log(res.data.message)
    //         this.lineChartOptions.xaxis.categories = res.data.message.dateaxis
    //         // this.lineChartOptions.xaxis.type = 'datetime';
    //         // this.lineChartOptions.xaxis.categories = res.data.message.dateaxis.map(dateStr => new Date(dateStr).getTime());
    //         this.lineData[0].data = res.data.message.line_start.data.positive
    //         this.lineData[1].data = res.data.message.line_start.data.neutral
    //         this.lineData[2].data = res.data.message.line_start.data.negative
    //         this.bar_start[0].data =res.data.message.bar_start
    //         console.log(this.lineChartOptions.xaxis.categories)

    //         // console.log(res.data.message.wordCloud.positive)
    //         // this.positiveWords= res.data.message.wordCloud.positive
    //         // this.negativeWords= res.data.message.wordCloud.negative
    //         // this.neutralWords= res.data.message.wordCloud.neutral
    //         // console.log(this.positiveWords)
    //         // console.log(this.negativeWords)
    //         // console.log(this.neutralWords)
            

    //         })
    // }


}
</script>

