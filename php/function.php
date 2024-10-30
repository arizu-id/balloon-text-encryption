<?php
function rand_str($length,$var='oO0'){
	$string = '';
	for($i = 0; $i < $length; $i++) {
		$pos = rand(0, strlen($var)-1);
		$string .= $var[$pos];
	}
	return $string;
}
function ozero_NEWencryption(){
	$jsonArray = json_decode(file_get_contents("words.json"), true);
	retry:
	$words = array();
	$words_hash = array();
	foreach ($jsonArray as $key => $value) {
		$rand = rand_str(10);
		$temps = json_encode($words_hash);
		if (in_array($rand, $words_hash)) {
			echo "[!] Some hashed value already added, trying..".PHP_EOL;
			goto retry;
		}
		$words[$key] = "$rand";
		$words_hash[$rand] = "$key";
	}
	file_put_contents('words_hash.json',json_encode($words_hash, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));
	file_put_contents('words.json',json_encode($words, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));
	return true;
}
function ozero_hash($text){
	$jsonArray = json_decode(file_get_contents("words.json"), true);
	$characters = str_split($text);
	$return = "";
	foreach ($characters as $char) {
		$return .= $jsonArray[$char];
	}
	return $return;
}
function ozero_decode($text){
	$jsonArray = json_decode(file_get_contents("words_hash.json"), true);
	$characters = str_split($text,10);
	$return = "";
	foreach ($characters as $char) {
		$return .= $jsonArray[$char];
	}
	return $return;
}
#ozero_NEWencryption();  //make new hash key data
$text = "Hello world, this is a balloon text encryption.";
$hashed = ozero_hash($text);
$unhash = ozero_decode($hashed);
echo "Text : $text\n";
echo "Encrypted : $hashed\n";
echo "Decrypted : $unhash\n";
