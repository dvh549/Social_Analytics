<template>
<!-- Area Chart -->
    <div class="row">
        <div class="col-xl-6 col-lg-7" >
                    <div class="card shadow mb-4">
                        <div
                            class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                            <h6 class="m-0 font-weight-bold text-primary">Sentiment-Correlation Analysis SG</h6>
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
                                        <td>0.802</td>
                                        <td>0.782</td>
                                    </tr>
                                    <tr>
                                        <td>Negative</td>
                                        <td>0.663</td>
                                        <td>0.691</td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2">Circuit</td>
                                        <td>Positive</td>
                                        <td>-0.515</td>
                                        <td>0.321</td>
                                    </tr>
                                    <tr>
                                        <td>Negative</td>
                                        <td>-0.469</td>
                                        <td>0.28</td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2">Phases</td>
                                        <td>Positive</td>
                                        <td>-0.044</td>
                                        <td>-0.135</td>
                                    </tr>
                                    <tr>
                                        <td>Negative</td>
                                        <td>0.223</td>
                                        <td>0.17</td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2">Acute</td>
                                        <td>Positive</td>
                                        <td>0.589</td>
                                        <td>0.634</td>
                                    </tr>
                                    <tr>
                                        <td>Negative</td>
                                        <td>0.577</td>
                                        <td>0.528</td>
                                    </tr>
                                    <tr>
                                        <td rowspan="2">Green</td>
                                        <td>Positive</td>
                                        <td>0.465</td>
                                        <td>0.606</td>
                                    </tr>
                                    <tr>
                                        <td>Negative</td>
                                        <td>-</td>
                                        <td>-</td>
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
                        Both positive and negative sentiments were strongly and moderately positively correlated respectively at the start of Covid-19, indicating that confirmed cases and deaths were big influences on the public’s sentiments and reactions.
                        <br/>

                        There was a notable drop after then from the circuit breaker to the different phases, indicating that people were less affected by the statistics as a result of confidence in governmental measures.
                        <br/>

                        For the acute to green phases, there was an increase in positive correlation likely due to the Omicron variant and the uncertainty surrounding how Singapore will transition to the new normal respectively.
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
