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
                        <img src="../assets/negative_wordcloud_cb_us.png" height="300px" style="margin:0 auto; display: block;">
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
                        <img src="../assets/neutral_wordcloud_cb_us.png" height="300px" style="margin:0 auto; display: block;">

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
                        <img src="../assets/positive_wordcloud_cb_us.png" height="300px" style="margin:0 auto; display: block;">

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
                            Positive tweets are the highest in proportion at 45%, followed by negative tweets at 33%, and neutral tweets at 22%. This indicated that the community agreed with the lockdown measures with tweets such as “Grateful for the comfort and peace of home. Stay safe. Stay vigilant. Stay focused. #grateful #takecareofyourself #stayhome #socialdistancing #covid-19 #strangetimes @ Washington D.C.”. 
                            <br/>
                            <strong>*Line Chart</strong>
                            <br/>
                            The number of opinions shared online dropped after the initial onset of the lockdown. 
                            <br/>
                            <strong>*Word Cloud</strong>
                            <br/>
                            However, there were many deaths ongoing as shown in the word cloud with “death” and “died” being one of the more prominent words. 
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
            bar_start:[{"name":'Sentiment',"data":[38,20,42]}],
            lineData:[
                {
                    "name":"Positive",
                    "data": [372,1316,1039,830,873,632,573,528,502,473,362,282,302,343,354,387,395,377,404,379,282,258,232,245,211,232,247,201,730,483,245,287,297,353,409,458,312,351,373,386,312,248,223,215,286,278,195,141,153,233,270,249,168,146,181,158,161,127,135,123,128,135,111,88,88,90,90,78,81,108,155,180,184,164,226,169,144,164,193,156,146,100,71,117,87,111,81,78,74,86,90,224,310,249,210,122,102,79,72,54,56,41,54,60,64,38,65,71,42,82,42]
                },
                {
                    "name":"Neutral",
                    "data": [208,670,623,440,490,323,302,271,266,234,185,105,136,174,153,167,206,179,176,176,129,134,81,123,91,113,98,93,346,253,125,146,127,179,194,194,167,176,195,222,128,114,143,101,151,108,79,73,87,83,82,91,85,79,73,85,82,65,59,57,59,66,50,37,51,32,31,48,40,66,69,104,67,76,76,92,68,69,85,67,62,50,50,59,46,46,33,42,46,36,36,125,134,108,100,52,60,29,27,33,13,21,22,18,38,16,29,19,23,24,25]
                },
                {
                    "name":"Negative",
                    "data": [260,882,819,652,670,526,415,427,346,346,354,256,243,314,305,350,371,351,331,395,273,250,226,247,179,273,228,211,614,523,218,294,255,265,315,349,312,353,417,367,292,340,235,194,292,219,212,197,156,196,214,193,153,118,135,160,185,138,87,67,100,89,93,81,94,90,99,80,86,127,165,209,166,188,193,193,154,212,261,168,188,137,119,142,94,93,72,73,71,80,70,184,237,253,209,135,104,77,70,51,37,37,36,33,46,29,47,45,43,63,27]
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
                    categories: ["2020-03-23","2020-03-30","2020-04-06","2020-04-13","2020-04-20","2020-04-27","2020-05-04","2020-05-11","2020-05-18","2020-05-25","2020-06-01","2020-06-08","2020-06-15","2020-06-22","2020-06-29","2020-07-06","2020-07-13","2020-07-20","2020-07-27","2020-08-03","2020-08-10","2020-08-17","2020-08-24","2020-08-31","2020-09-07","2020-09-14","2020-09-21","2020-09-28","2020-10-05","2020-10-12","2020-10-19","2020-10-26","2020-11-02","2020-11-09","2020-11-16","2020-11-23","2020-11-30","2020-12-07","2020-12-14","2020-12-21","2020-12-28","2021-01-04","2021-01-11","2021-01-18","2021-01-25","2021-02-01","2021-02-08","2021-02-15","2021-02-22","2021-03-01","2021-03-08","2021-03-15","2021-03-22","2021-03-29","2021-04-05","2021-04-12","2021-04-19","2021-04-26","2021-05-03","2021-05-10","2021-05-17","2021-05-24","2021-05-31","2021-06-07","2021-06-14","2021-06-21","2021-06-28","2021-07-05","2021-07-12","2021-07-19","2021-07-26","2021-08-02","2021-08-09","2021-08-16","2021-08-23","2021-08-30","2021-09-06","2021-09-13","2021-09-20","2021-09-27","2021-10-04","2021-10-11","2021-10-18","2021-10-25","2021-11-01","2021-11-08","2021-11-15","2021-11-22","2021-11-29","2021-12-06","2021-12-13","2021-12-20","2021-12-27","2022-01-03","2022-01-10","2022-01-17","2022-01-24","2022-01-31","2022-02-07","2022-02-14","2022-02-21","2022-02-28","2022-03-07","2022-03-14","2022-03-21","2022-03-28","2022-04-04","2022-04-11","2022-04-18","2022-04-25","2022-05-02"],
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
    //     await axios.get("http://127.0.0.1:5000/getSentimentAnalysisCBUS")
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

