
import React, {useState} from 'react'

// class Counter extends React.Component{
//     constructor(props){
//         super(props);
//         this.state = {
//             count: 0
//         }

//         this.incrementCounter = this.incrementCounter.bind(this)
//     }

//     incrementCounter(){
//         this.setState((state, props) => {
//             return {
//                 count: state.count + 1
//             }
//         })
//         console.log(this.state.count)
//     }

//     decrementCounter = () => {
//         this.setState((state, props) => {
//             return {
//                 count:  state.count > 0 ? state.count - 1 : 0
//             }
//         })
//         console.log(this.state.count)
//     }

//     render(){
//         return ( 
//         <div>
//           <h2>Counter: {this.state.count} </h2>  <br />
//           <div >
//                 <button type="button" onClick={this.incrementCounter} >Increment +</button>
//                 <span> </span>
//                 <button type="button" onClick={this.decrementCounter} >Decrement -</button>
//           </div>
//         </div> )
//     }
// }


// export default Counter;

function Counter() {
    const [count, setCount] = useState(0);

    function incrementCounter(){
        setCount(count => count + 1)
        console.log(count)
    }
    function decrementCounter(){
        setCount(count => count > 0 ? count - 1 : 0)
        console.log(count)
    }

  return (
    <div>
    <h2>Counter: {count} </h2>  <br />
    <div >
          <button type="button" onClick={incrementCounter} >Increment +</button>
          <span> </span>
          <button type="button" onClick={decrementCounter} >Decrement -</button>
    </div>
  </div> )
  
}

export default Counter