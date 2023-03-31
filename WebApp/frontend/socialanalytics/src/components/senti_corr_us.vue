<template>
<!-- Area Chart -->
    <div class="row">
        <div class="col-xl-6 col-lg-7" >
                    <div class="card shadow mb-4">
                        <div
                            class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                            <h6 class="m-0 font-weight-bold text-primary">Sentiment-Correlation Analysis US</h6>
                        </div>
                        <div class="card-body" style="height:700px">
                            <div class="chart-area">
                                <table style="height:600px; width:100%">
                                    <tr>
                                        <th>Time Period</th>
                                        <th>Sentiment</th>
                                        <th>Cases</th>
                                        <th>Death</th>
                                    </tr>
                                    <tr>
                                        <td rowspan="2">Start</td>
                                        <td>Positive</td>
                                        <td>0.634</td>
                                        <td>0.68</td>
                                    </tr>
                                    <tr>
                                        <td>Negative</td>
                                        <td>0.587</td>
                                        <td>0.639</td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2">Lockdown</td>
                                        <td>Positive</td>
                                        <td>0.437</td>
                                        <td>0.097</td>
                                    </tr>
                                    <tr>
                                        <td>Negative</td>
                                        <td>0.533</td>
                                        <td>0.184</td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2">2020</td>
                                        <td>Positive</td>
                                        <td>0.003</td>
                                        <td>-0.025</td>
                                    </tr>
                                    <tr>
                                        <td>Negative</td>
                                        <td>0.134</td>
                                        <td>0.1</td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2">2021</td>
                                        <td>Positive</td>
                                        <td>0.537</td>
                                        <td>0.527</td>
                                    </tr>
                                    <tr>
                                        <td>Negative</td>
                                        <td>0.629</td>
                                        <td>0.64</td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2">2022</td>
                                        <td>Positive</td>
                                        <td>0.343</td>
                                        <td>0.112</td>
                                    </tr>
                                    <tr>
                                        <td>Negative</td>
                                        <td>0.327</td>
                                        <td>0.109</td>
                                    </tr>
                                </table>

                            </div>
                        </div>
                    </div>
                </div>

        <div class="col-xl-6 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Analysis</h6>
                </div>
                <div class="card-body" style="height:700px; overflow-y: scroll;">
                    <div class="chart-area">
                        <p>
                        From the correlation values of each period, we observed the following:
                        <br/>
                        <br/>
                        Similar to Singapore, correlation between sentiments and cases/death respectively were highest at the start, indicating the influences that confirmed cases and deaths had on public sentiments.
                        <br/>
                        <br/>

                        For the different phases however, we noticed consistency in moderate correlations, which was a result of the public’s discontentment with governmental measures that was tied with the much higher number of confirmed cases and deaths experienced in the US compared to SG
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    

    



</template>

<script>
import 'vis-network/styles/vis-network.css'
// import { Network } from "vis-network/peer/esm/vis-network";
// import { DataSet } from "vis-data/peer/esm/vis-data"
// import jsonData from "../assets/nodeJson.json"
// import {CovidNode} from '../config.js'
export default {
    props: {
        // positiveWordsComponent: Array,
        // negativeWordsComponent: Array,
        // neutralWordsComponent: Array
       
    },
    components: {
        // SocialNetwork
        // Network
    },
    data(){
        return{
        

        }
  }, 
    mounted() {
        // const container = this.$refs.graph
        // var nodes = new DataSet(jsonData.nodes)
        // var edges = new DataSet(jsonData.edges)

        // const data = {
        // nodes: nodes,
        // edges: edges
        // }
        // const options = {
        //      interaction: {
        //         navigationButtons: true,
        //         zoomView: true, // Enable zooming
        //         dragView: true, // Enable panning 
        //     },
        //     layout:{
        //         improvedLayout:false
        //     },
        //      nodes: {
        //         size: 10
        //     }
            

        // }
        // console.log("HERE")
        // // new Network(container, data, options)
        // var network = new Network(container, data, options)
        // this.network= network
        // this.zoomToNode(2);
            
        

    },
    methods: {
        //  zoomToNode(nodeId) {
            
        //         var position = this.network.getPositions()[nodeId];
        //         this.network.focus(2,{
        //             position: {x:position.x, y:position.x},
        //             offset: position,
        //             scale: 1,
        //             locked: false,
        //         });
           
        // },
        
    }


}
</script>

<style scoped>
    table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
    
    }
</style>
