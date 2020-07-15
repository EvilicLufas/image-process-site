class VideoPanel extends React.Component {
    constructor(props){
        super(props);
        this.state = {status: "No Status"};
    }

    render(){
        return(
            <h1>{this.state.status}</h1>
        );
    }

    stateSelector(){
        console.log("checking state")
        console.log(document.getElementById('video').getAttribute("data-status"));
        if (document.getElementById('video').getAttribute("data-status") == "downloading_video"){
            console.log("entered first");
            this.setState({status:'Downloading Video'});
        } else if (document.getElementById('video').getAttribute("data-status") == "processing_video"){
            console.log("entered second");
            this.setState({status:'Processing Video'});
        } else {
            this.setState({status:'Completed'});
            clearInterval(this.timerID);
            console.log("no longer checking process status");
        }
    }

    componentDidMount() {
        this.timerID = setInterval(
            ()=> this.stateSelector(), 
            2000
        );
    }

    componentWillUnmount() {
        clearInterval(this.timerID)
    }
}

ReactDOM.render(
    <VideoPanel />,
    document.getElementById('video')
);
ReactDOM.render(
    <VideoPanel />,
    document.getElementById('video_one')
)