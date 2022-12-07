
<script>
	import { onMount } from "svelte"
	let logs = ""
	let pods=[]
	let message_count = 0

	onMount( () => {
		const evtSrc = new EventSource("http://localhost:3500/event")
		evtSrc.onmessage = function(event) {
			
			logs = event.data
			message_count += 1
			// if(pods.includes(logs['podname'])){
			// 	pods[]
			// }else{
			// 	let value = {}
			// 	value.logs['podname']:0
			// 	pods.push({logs['podname']:0})
			// }
		}

		evtSrc.onerror = function(event) {
			console.log(event)
		}
	})

	async function fetchLogs() {
		const res = await fetch("http://localhost:3500/time")
		if (res.status !== 200) {
			console.log("Could not connect to the server")
		} else {
			console.log("OK")
		}
	}
</script>

<main>
	<h1>Hyper Execute</h1>
	<button on:click="{ fetchLogs }">Fetch logs</button>
	<!-- <p>logs: { JSON.stringify(logs) }</p> -->
	<p>logs: {logs}</p>
	<p>count: {message_count}</p>
</main>